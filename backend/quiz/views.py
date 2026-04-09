from rest_framework.views import APIView, Response, status
from words.models import UserWord
from .models import Quiz
from .serializers import GenerateQuizSerializer
from rest_framework.permissions import IsAuthenticated

### Quiz actions
#- Quiz starts -> POST /quiz/start/
#- Quiz ends -> POST /quiz/end/
#- Mcq solved -> POST /quiz/mcq/solve
#- Quiz generates -> POST /quiz/generate

class GenerateQuizView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print("CALLED")
        user = request.user
        # if not user.is_authenticated:
        #     return JsonResponse({'detail': 'Authentication required'}, status=401)
        words = UserWord.objects.filter(user=user).select_related('word')
        data = [
            {
                'word': w.word.text,
                'status': w.status,
                'score': w.score,
            }
            for w in words
        ]
        print("Words", data)
        quiz = Quiz.objects.create(user=user)
        quiz.save()
        print(quiz.id)
        return Response({'id': quiz.id, 'words': data}, status=status.HTTP_201_CREATED)

class StartQuiz(APIView):
    def post(self, request):
       ... 

class EndQuiz(APIView):
    def post(self, request):
        ...

class McqSolved(APIView):
    def post(self, request):
        ...
