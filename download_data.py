import torchvision
from torchvision.transforms import ToTensor
def download_dataset():
    mnist = torchvision.datasets.MNIST(root='data', download=True)
    print('length of MNIST', len(mnist))
    id = 4
    img, label = mnist[id]
    print(img)
    print(label)

    # On computer with monitor
    img.show()


    img.save('tmp.jpg')
    tensor = ToTensor()(img)
    print(tensor.shape)
    print(tensor.max())
    print(tensor.min())

if __name__ == '__main__':
    download_dataset()