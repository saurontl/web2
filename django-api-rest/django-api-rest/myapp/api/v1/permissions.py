from rest_framework.permissions import BasePermission

class IsClientOwner(BasePermission):
    """
    Permite acesso apenas ao cliente dono do pedido.
    """

    def has_object_permission(self, request, view, obj):
        # Supondo que o modelo Order tem um campo 'client' que é um FK para Client
        return obj.client.user == request.user