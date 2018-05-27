package turtle_princeton;

/******************************************************************************
 *  컴파일:  javac Rect_Triangle.java
 *  의존성:  StaDraw.java
 *
 ******************************************************************************/

import java.awt.Color;

public class Turtle {
    /** 인스턴스 변수 */
    private double x, y;     // 거북이의 초기 위치 좌표값: (x, y)
    private double angle;    // 거북이가 처음에 바라보는 방향: x-축으로부터 반시계방향으로 잰 각도

    /** Turtle 클래스 생성자
    	3 개의 인자 사용: 초기 위치 좌표값 (x0, y0) 및 바라보는 방향 */
    public Turtle(double x0, double y0, double a0) {
        x = x0;
        y = y0;
        angle = a0;
    }
    
    /** 인스턴스 메소드 */
    
    // 지정된 거리만큼 바라보는 방향으로 전진하기(픽셀 기준)
    public void goForward(double step) {
        double oldx = x;
        double oldy = y;
        x += step * Math.cos(Math.toRadians(angle));
        y += step * Math.sin(Math.toRadians(angle));
        StdDraw.line(oldx, oldy, x, y);
    }

    // 반시계 방향으로 지정된 각도만큼 회전하기
    public void turnLeft(double delta) {
        angle += delta;
    }

    // 지정된 시간(1000분의 1초 기준) 동안 멈추기
    public void pause(int t) {
        StdDraw.pause(t);
    }

    // 선 색깔 지정하기
    public void setPenColor(Color color) {
        StdDraw.setPenColor(color);
    }

    // 선 두께 지정하기
    public void setPenRadius(double radius) {
        StdDraw.setPenRadius(radius);
    }
    
}