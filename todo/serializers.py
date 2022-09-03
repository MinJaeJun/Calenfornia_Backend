from rest_framework import serializers # 시리얼라이저를 불러옵니다.
from .models import Todo #, Todos 모델을 불러옵니다.

# 전체 조회: id, 설명, 완료 여부, 중요 여부
class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user_id', 'description', 'complete')

# 상세 조회: id, 설명, 완료 여부, 중요 여부 
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user_id', 'description', 'created', 'complete')

# 생성
class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('user_id', 'description')

# 수정 할 부분
# class TodoSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Todos
#        fields = ['id', 'description', 'complete']