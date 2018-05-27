package turtle_princeton;

/******************************************************************************
 *  컴파일:  javac Rectangle.java
 *  실행:   java Rectangle
 *  의존성:  Turtle.java, StaDraw.java
 *
 ******************************************************************************/

public class Rectangle {

    public static void main(String[] args) {
    	
    	// 캔버스 설정
    	StdDraw.setCanvasSize(600,600);				// 캔버스 사이즈 지정 
        StdDraw.setXscale(-1, 1);					// 캔버스 X 좌표 스케일 기준 설정하기 
        StdDraw.setYscale(-1, 1);					// 캔버스 X, Y 좌표 스케일 기준 설정하기 
        
        // 거북이 인스턴스 생성하기
        double step = 1;							// 이동 거리 
        double x0 = -step/2;						// 초기 위치 x 좌표값 
        double y0 = -0.4;							// 초기 위치 y 좌표값 
        double a0 = 0.0;							// 초기 바라보는 방향 
        Turtle turtle = new Turtle(x0, y0, a0);		// 거북이 인스턴스 생성 
        
        // 정사각형 그리기 
        int count = 0;
        while (count < 4) {							// 4번 반복
	        turtle.goForward(step);						// step 만큼 전
	        turtle.turnLeft(90.0);						// 시계반대 방향으로 90도 회전
	        count++;
        }
    }
}