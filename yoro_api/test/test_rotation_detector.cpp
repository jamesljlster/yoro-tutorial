#include <cmath>
#include <iostream>
#include <opencv2/opencv.hpp>

#include <yoro_api.hpp>

using namespace yoro_api;
using namespace std;
using namespace cv;

void draw_angle(Mat& image, float angle);

int main(int argc, char* argv[])
try
{
    // Check arguments
    if (argc < 3)
    {
        printf("Usage: %s <model_path> <test_image> [device]\n", argv[0]);
        return -1;
    }

    DeviceType devType = DeviceType::Auto;
    if (argc > 3)
    {
        if (string(argv[3]) == "cpu")
        {
            devType = DeviceType::CPU;
        }
        else if (string(argv[3]) == "cuda")
        {
            devType = DeviceType::CUDA;
        }
    }

    // Import model and load image
    RotationDetector detector(argv[1], devType);
    Mat image = imread(argv[2], IMREAD_COLOR);

    // Run detection
    float pred = detector.detect(image);

    // Show result
    cout << "Detection: " << pred << endl;
    draw_angle(image, pred);

    imshow("Detection Result", image);
    waitKey(0);

    return 0;
}
catch (exception& ex)
{
    cout << "Error occurred:" << endl;
    cout << ex.what() << endl;
    return -1;
}

void draw_angle(Mat& image, float angle)
{
    float length = min(image.rows, image.cols) * 3 / 8;
    float rad = (angle + 90) * 3.14159265358979323846 / 180;
    Point ctr = Point(image.cols / 2, image.rows / 2);
    arrowedLine(
        image,
        ctr,
        ctr + Point((int)(length * cos(rad)), (int)(-length * sin(rad))),
        Scalar(0, 85, 255),
        2,
        LINE_AA);
}
