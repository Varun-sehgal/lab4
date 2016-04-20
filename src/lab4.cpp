#include "eecs230.h"

struct Point2D{
    double x;
    double y;
};

struct LineSegment{
    Point2D point1;
    Point2D point2;
    LineSegment(){}

    LineSegment (double x1, double y1, double x2, double y2){
        point1.x = x1;
        point1.y = y1;
        point2.x = x2;
        point2.y = y2;
    }
};


struct Date {
    int  year;
    int  month;
    int  day;
    bool is_AD;

    Date(int y, int m, int d, bool ad)
    {
        year  = y;
        month = m;
        day   = d;
        is_AD = ad;
    };
};

class DateClass{
public:
    int year;
    int month;
    int day;
    bool is_AD;
    DateClass(){}
    DateClass(int y, int m, int d, bool ad){
        year = y;
        month = m;
        day = d;
        is_AD = ad;
    };
private:

};

LineSegment LineSegmentAddition(LineSegment line1, LineSegment line2){
    LineSegment ret;
    ret.point1.x = line1.point1.x + line2.point1.x;
    ret.point1.y = line1.point1.y + line2.point1.y;

    ret.point2.x = line1.point2.x + line2.point2.x;
    ret.point2.y = line1.point2.y + line2.point2.y;

    return ret;

}
int main()
try
{
    LineSegment line1 = LineSegment(1,1,2,2);
    LineSegment line2 = LineSegment(1,2,2,1);

    /*
    line1.point1.x = 1;
    line1.point1.y = 1;
    line1.point2.x = 2;
    line1.point2.y = 2;
    line2.point1.x = 1;
    line2.point1.y = 2;
    line2.point2.x = 2;
    line2.point2.y = 1;
    */
    LineSegment add = LineSegmentAddition(line1, line2);

    cout << "point1.x: " << add.point1.x << " point1.y:" << add.point1.y << endl;

    cout << "point2.x: " << add.point2.x << " point1.y:" << add.point2.y << endl;
}

catch (runtime_error& e) {
    cerr << "Caught in main: " << e.what() << "\n";
    exit(1);
}
