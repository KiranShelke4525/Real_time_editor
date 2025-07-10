from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Document
from .serializers import DocumentSerializer 
import requests



class LanguageToolCorrectView(APIView):
    def post(self, request):
        text = request.data.get("text", "")
        if not text:
            return Response({"error": "No text provided."}, status=400)

        try:
            res = requests.post(
                "https://api.languagetool.org/v2/check",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={"text": text, "language": "en-US"},
            )

            result = res.json()
            matches = result.get("matches", [])

            corrected = text
            shift = 0

            for match in sorted(matches, key=lambda x: x["offset"]):
                if not match["replacements"]:
                    continue

                replacement = match["replacements"][0]["value"]
                offset = match["offset"] + shift
                length = match["length"]
                corrected = corrected[:offset] + replacement + corrected[offset + length:]
                shift += len(replacement) - length

            return Response({"corrected_text": corrected})

        except Exception as e:
            return Response({"error": str(e)}, status=500)


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "User registered successfully"}, status=201)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=401)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email
        })

class MyDocumentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        documents = Document.objects.filter(user=request.user)
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)


