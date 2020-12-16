import torch
from torch import nn


class DemoCNN(nn.Module):

    """ DemoCNN: A CNN network modified from AlexNet """

    def __init__(self, num_classes, in_channels=3):

        super(DemoCNN, self).__init__()

        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),

            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),

            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),

            nn.AdaptiveAvgPool2d((7, 7))
        )

        self.classifier = nn.Sequential(
            nn.Linear(7 * 7 * 256, 1024),
            nn.Linear(1024, 1024),
            nn.Linear(1024, num_classes)
        )

    def forward(self, x):

        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)

        return x


class DemoFCN(nn.Module):

    """ DemoFCN: A FCN network modified from AlexNet """

    def __init__(self, in_channels=3):

        super(DemoFCN, self).__init__()

        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),

            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),

            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )

    def forward(self, x):
        return self.features(x)


if __name__ == '__main__':

    # Random test image
    src = torch.randn((1, 3, 224, 224))

    # Test and check if given model is torchscript compatible
    model = torch.jit.script(DemoCNN(num_classes=2))
    out = model(src)

    model = torch.jit.script(DemoFCN())
    out = model(src)
