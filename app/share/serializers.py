from rest_framework import serializers
from routines.serializers import OnlyRoutineSerializer, RoutineSerializer
from accounts.serializers import PublicProfileSerializer
from .models import ShareRoutineUser, ShareRoutinePublic


class ShareRoutineUserSerializer(serializers.ModelSerializer):
    """ Serializer to routines shared with user """
    routine = OnlyRoutineSerializer(
        read_only=True,
    )
    owner = PublicProfileSerializer(
        read_only=True,
    )

    class Meta:
        model = ShareRoutineUser
        fields = [
            'id',
            'routine',
            'owner',
            'occupant',
        ]


class ShareRoutineUserDetailSerializer(serializers.ModelSerializer):
    """ Serializer to routines shared with user """
    routine = RoutineSerializer(
        read_only=True,
    )
    owner = PublicProfileSerializer(
        read_only=True,
    )

    class Meta:
        model = ShareRoutineUser
        fields = [
            'id',
            'routine',
            'owner',
            'occupant',
        ]


class ShareRoutinePublicSerializer(serializers.ModelSerializer):
    """ Serializer to routines shared with the public """
    routine = RoutineSerializer(
        read_only=True,
    )
    owner = PublicProfileSerializer(
        read_only=True,
    )

    class Meta:
        model = ShareRoutinePublic
        fields = [
            'routine',
            'owner',
            'id',
        ]
