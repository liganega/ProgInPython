package turtle_princeton;

/******************************************************************************
 *  컴파일:  javac Rect_Triangle.java
 *  실행:   java Rect_Triangle
 *  의존성:  Turtle.java, StaDraw.java
 *
 ******************************************************************************/

public class Rect_Triangle {

    public static void main(String[] args) {
    	
    	// 캔버스 설정
    	StdDraw.setCanvasSize(600,600);					// 캔버스 사이즈 지정 
        StdDraw.setXscale(-1, 1);						// 캔버스 X 좌표 스케일 기준 설정하기 
        StdDraw.setYscale(-1, 1);						// 캔버스 X, Y 좌표 스케일 기준 설정하기 
        StdDraw.setPenColor(StdDraw.BLUE);				// 펜 색깔 지정: BLUE
        												// 펜 색깔은 모든 거북이 인스턴스에 적용됨
        
        // 거북이 인스턴스 생성하기
        double step = 1;								// 이동 거리 
        double x0 = -step/2;							// 초기 위치 x 좌표값 
        double y0 = -0.4;								// 초기 위치 y 좌표값 
        double a0 = 0.0;								// 초기 바라보는 방향 
        Turtle turtle_tri = new Turtle(x0, y0, a0);		// 첫째 거북이 인스턴스 생성 
        Turtle turtle_rect = new Turtle(x0, y0, a0);	// 둘째 거북이 인스턴스 생성 
        
        // 정삼각형 그리기 
        int count1 = 0;
        while (count1 < 3) {							// 3번 반복
	        turtle_tri.goForward(step);						// step 만큼 전
	        turtle_tri.turnLeft(120.0);						// 시계반대 방향으로 120도 회전
	        count1++;
        }
        // 정사각형 그리기 
        int count2 = 0;
        while (count2 < 4) {							// 4번 반복
	        turtle_rect.goForward(step);					// step 만큼 전
	        turtle_rect.turnLeft(90.0);						// 시계반대 방향으로 90도 회전
	        count2++;
	    }
    }
}