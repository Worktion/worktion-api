from rest_framework import serializers
from .models import Routine, ExecutionBlock, ExecutionExercise
from exercises.serializers import ExerciseSerializer


class ExecutionExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = ExecutionExercise
        fields = [
            'id',
            'quantity',
            'typeExecution',
            'exercise',
        ]


class ExecutionBlockSerializer(serializers.ModelSerializer):
    exercises = ExecutionExerciseSerializer(
        source='executions_block',
        many=True,
    )

    class Meta:
        model = ExecutionBlock
        fields = ['id', 'name', 'quantity', 'exercises']


class RoutineSerializer(serializers.ModelSerializer):
    blocks = ExecutionBlockSerializer(
        source='blocks_routine',
        many=True,
    )

    class Meta:
        model = Routine
        fields = [
            'id',
            'name',
            'description',
            'is_public',
            'time',
            'created',
            'dificulty',
            'muscle_group',
            'cover',
            'blocks',
        ]
