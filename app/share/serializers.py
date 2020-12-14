from rest_framework import serializers
from routines.serializers import OnlyRoutineShareSerializer, RoutineSerializer
from routines.models import Routine
from accounts.serializers import PublicProfileSerializer
from .models import ShareRoutineUser, ShareRoutinePublic
from django.contrib.auth import get_user_model

User = get_user_model()


class ShareRoutineUserSerializer(serializers.ModelSerializer):
    """ Serializer to routines shared with user """
    routine = OnlyRoutineShareSerializer(read_only=True)
    owner = PublicProfileSerializer(read_only=True)
    occupant_email = serializers.CharField(write_only=True)
    routine_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ShareRoutineUser
        fields = [
            'id',
            'routine',
            'owner',
            'routine_id',
            'occupant_email',
        ]

    def validate(self, data):
        _email = data['occupant_email']
        if not User.objects.filter(email=_email).exists():
            raise serializers.ValidationError({"occupant_email": "User not found"})
        _routine = data['routine_id']
        if not Routine.objects.filter(id=_routine).exists():
            raise serializers.ValidationError({"routine_id": "Routine not found"})
        _owner = self.context['request'].user
        if _owner.id != Routine.objects.get(id=_routine).user.id:
            raise serializers.ValidationError({
                "Permissions": "Yo don't have permission for this routine"
            })

        return data

    def create(self, validated_data):
        _owner = self.context['request'].user
        _occupant = User.objects.get(
            email=validated_data.get('occupant_email'),
        )
        _routine = Routine.objects.get(
            id=validated_data.get('routine_id'),
        )
        share = ShareRoutineUser.objects.create(
            routine=_routine,
            owner=_owner,
            occupant=_occupant,
        )
        return share


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
    routine_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ShareRoutinePublic
        fields = [
            'routine',
            'owner',
            'id',
            'routine_id',
        ]

    def validate(self, data):
        _routine = data['routine_id']
        if not Routine.objects.filter(id=_routine).exists():
            raise serializers.ValidationError({"routine_id": "Routine not found"})
        _owner = self.context['request'].user
        if _owner.id != Routine.objects.get(id=_routine).user.id:
            raise serializers.ValidationError({
                "Permissions": "Yo don't have permission for this routine"
            })

        return data

    def create(self, validated_data):
        _owner = self.context['request'].user
        _routine = Routine.objects.get(
            id=validated_data.get('routine_id'),
        )
        share = ShareRoutinePublic.objects.create(
            routine=_routine,
            owner=_owner,
        )
        return share
