from rest_framework import serializers
from .models import Routine, ExecutionBlock, ExecutionExercise
from exercises.serializers import ExerciseSerializer
from exercises.models import Exercise


class ExecutionExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    exercise_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ExecutionExercise
        fields = [
            'id',
            'quantity',
            'typeExecution',
            'exercise',
            'exercise_id',
        ]


class WriteExecutionBlockSerializer(serializers.ModelSerializer):
    exercises = ExecutionExerciseSerializer(
        many=True,
    )

    class Meta:
        model = ExecutionBlock
        fields = ['id', 'name', 'quantity', 'exercises']


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


class OnlyRoutineSerializer(serializers.HyperlinkedModelSerializer):
    routine_detail = serializers.HyperlinkedIdentityField(view_name='routine_detail')
    blocks = WriteExecutionBlockSerializer(
        many=True,
        write_only=True,
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
            'routine_detail',
            'blocks',
        ]

    def create(self, validated_data):
        _user = self.context['request'].user
        list_blocks = validated_data.pop('blocks')
        print(list_blocks)
        _routine = Routine.objects.create(
            user=_user,
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            is_public=validated_data.get('is_public'),
            time=validated_data.get('time'),
            dificulty=validated_data.get('dificulty'),
            muscle_group=validated_data.get('muscle_group'),
        )
        for block in list_blocks:
            list_exercises = block.pop('exercises')
            print(list_exercises)
            _block = ExecutionBlock.objects.create(
                routine=_routine,
                name=block.get('name'),
                quantity=block.get('quantity'),
            )
            for exercise in list_exercises:
                print('Ejercicio: ' + str(exercise.get('exercise_id')))
                _exercise = Exercise.objects.get(
                    id=exercise.get('exercise_id')
                )
                ExecutionExercise.objects.create(
                    execution_block=_block,
                    exercise=_exercise,
                    quantity=exercise.get('quantity'),
                    typeExecution=exercise.get('typeExecution'),
                )
        return _routine


class OnlyRoutineShareSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Routine
        fields = [
            'id',
            'name',
            'description',
            'time',
            'dificulty',
            'muscle_group',
            'cover',
        ]
