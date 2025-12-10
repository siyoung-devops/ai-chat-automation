pipeline {
a
gen
t a
ny
sta
ges {
sta
}
}
sta
ge('Hello') {
steps {
echo 'Hello World'
echo 'Jenkins Pipeline에 오신 것을 환영합니다!'
ge('Build') {
steps {
echo 'Building...'
echo "빌드 번호: ${env.BUILD_NUMBER}"
echo "Job 이름: ${env.JOB_NAME}"
sh 'ls -la'
}
sta
}
ge('Test') {
steps {
echo 'Testing...'
sh '''
echo "테스트를 시작합니다"
echo "현재 시간: $(date)"
echo "테스트 완료!"
'''
}
sta
}
ge('Deploy') {
steps {
echo 'Deploying...'
echo '배포가 완료되었습니다!'
}
}
}
post {
success {
echo '파이프라인이 성공적으로 완료되었습니다!'
}
f
ailure {
echo '파이프라인 실행 중 오류가 발생했습니다.'
}
always {
echo '파이프라인 실행이 종료되었습니다.'
}
}
}
