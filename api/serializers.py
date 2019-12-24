from rest_framework import serializers

from .models import Question,Answer

class QuestionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=20)
    email=serializers.EmailField()
    question=serializers.CharField()

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id=validated_data.get('id',instance.id)
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.question=validated_data.get('question',instance.question)

        instance.save()

        return instance


class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    answer = serializers.CharField()
    question_id=serializers.IntegerField()

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.question_id=validated_data.get('question_id',instance.question_id)

        instance.save()

        return instance
