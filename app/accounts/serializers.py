""" Imports """
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    """ Serializer of Login """
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    refresh = serializers.UUIDField(read_only=True)
    access = serializers.UUIDField(read_only=True)
    email_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'refresh', 'access', 'email_verified']

    def create(self, validated_data):
        try:
            user_tokens = User.objects.login(
                validated_data['email'],
                validated_data['password']
            )
            return user_tokens
        except ValueError as error:
            raise serializers.ValidationError({"value_error": error})
        except Exception as error:
            raise serializers.ValidationError({"email_not_verified": error})


class RecoverPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        write_only=True,
    )

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email']).first()
        user.send_email_recover_password()
        return user

    def validate_email(self, email):
        """ Validation if email is in a account """
        exist_email = User.objects.filter(email=email).exists()
        if not exist_email:
            raise serializers.ValidationError("User not found with the input email")
        return email


class ValidateCodeRecoverPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    code = serializers.IntegerField(required=True, write_only=True)
    access_token = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email']).first()
        try:
            token = user.validate_code_recover_pass(validated_data['code'])
            return {
                'access_token': str(token)
            }
        except Exception as ex:
            raise serializers.ValidationError(ex)

    def validate_email(self, email):
        """ Validation if email is in a account """
        exist_email = User.objects.filter(email=email).exists()
        if not exist_email:
            raise serializers.ValidationError("User not found with the input email")
        return email


class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)

    def create(self, validated_data):
        user = self.context['request'].user
        user.update_password(validated_data['password'])
        return True


class UserSerializer(serializers.ModelSerializer):
    """ Serializer of model CustomUser  """
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    username = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
        )
        return user


class ConfirmEmailSerializer(serializers.ModelSerializer):
    """ Serializer to confirm the email """
    email_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['email_verified']

    def create(self, validated_data):
        user = self.context['request'].user
        user.validate_email()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer to the User Profile """

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'bio',
            'birth_date',
            'cover',
        ]


class PublicProfileSerializer(serializers.ModelSerializer):
    """ Serializer to the User Profile for public users """

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'cover',
        ]
