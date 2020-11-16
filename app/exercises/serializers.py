from rest_framework import serializers
from .models import Exercise, ExerciseImage


class ExerciseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseImage
        fields = ['image']


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    images = ExerciseImageSerializer(source='exercise_images', many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'similar_names',
            'description',
            'dificulty',
            'images',
        ]

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        exercise = Exercise.objects.create(
            name=validated_data.get('name'),
            similar_names=validated_data.get('similar_names'),
            description=validated_data.get('description'),
            dificulty=validated_data.get('dificulty'),
        )
        for image in images_data.values():
            ExerciseImage.objects.create(
                exercise=exercise,
                image=image
            )
        return exercise
