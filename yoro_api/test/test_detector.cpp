#include <cmath>
#include <iostream>
#include <opencv2/opencv.hpp>

#include <yoro_api.hpp>

using namespace yoro_api;
using namespace std;
using namespace cv;

void draw_rbox(Mat& image, const RBox& rbox);

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
    YORODetector detector(argv[1], devType);
    Mat image = imread(argv[2], IMREAD_COLOR);

    // Run detection
    vector<RBox> pred = detector.detect(image, 0.9, 0.7);

    // Show result
    for (size_t i = 0; i < pred.size(); i++)
    {
        cout << pred[i].to_string() << endl;
        draw_rbox(image, pred[i]);
    }

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

void draw_rbox(Mat& image, const RBox& rbox)
{
    // Convert yoro_api::RBox to cv::RotatedRect
    RotatedRect rRect(
        Point2f(rbox.x, rbox.y), Size2f(rbox.w, rbox.h), -rbox.degree);

    // Draw rotated bounding box
    Point2f boxPts[4];
    rRect.points(boxPts);
    for (size_t i = 0; i < 4; i++)
    {
        // Draw bounding box
        line(
            image,
            boxPts[i],
            boxPts[(i + 1) % 4],
            Scalar(0, 128, 0),
            2,
            LINE_AA);

        // Draw arrow
        float length = rbox.h * 3 / 8;
        float rad = (rbox.degree + 90) * 3.14159265358979323846 / 180;
        Point ctr = Point((int)rbox.x, (int)rbox.y);
        arrowedLine(
            image,
            ctr,
            ctr + Point((int)(length * cos(rad)), (int)(-length * sin(rad))),
            Scalar(192, 0, 0),
            2,
            LINE_AA,
            0,
            0.2);

        // Draw label
        float shift = rbox.h / 4;
        putText(
            image,
            to_string(rbox.label),
            ctr - Point((int)(shift * cos(rad)), (int)(-shift * sin(rad))),
            FONT_HERSHEY_SIMPLEX,
            0.7,
            Scalar(0, 0, 0),
            2,
            LINE_AA);
    }
}
