from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor, Categoria, Editora, Livro
from livraria.serializers import (AutorSerializer, CategoriaSerializer,
                                  EditoraSerializer, LivroDetailSerializer,
                                  LivroSerializer, LivroListSerializer )


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
    

