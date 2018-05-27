package turtle_princeton;

public class No_Graphic {

    public static void main(String[] args) {
        // 거북이 인스턴스 생성하기
        double step = 1;							   // 이동 거리 
        double x0 = -step/2;						   // 초기 위치 x 좌표값 
        double y0 = -0.4;							  // 초기 위치 y 좌표값 
        double a0 = 0.0;							   // 초기 바라보는 방향 
        Turtle turtle_tri = new Turtle(x0, y0, a0);	// 첫째 거북이 인스턴스 생성 
    }

}
