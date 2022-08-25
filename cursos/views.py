from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Avaliacao, Curso
from .serializers import Avaliacao, AvaliacaoSerializer, Curso, CursoSerializer


class CursoAPIView(APIView):
    """
    API de curso da Geek
    """
    def get(selt, request):
        # print(request.user)
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({"msg" : "Criado com sucesso!"}, status=status.HTTP_201_CREATED)
        # return Response({"id": serializer.data['id'], "curso": serializer.data['titulo']}, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliações da Geek
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
