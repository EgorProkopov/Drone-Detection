import os
import shutil
import numpy as np

from sklearn.model_selection import train_test_split


frames_folder_path_source = 'train_dataset\\images'
labels_folder_path_source = 'train_dataset\\labels'


def save_dataset(dataset, path_destination, frames=True):
    for file_name in dataset:
        if frames:
            file_source = frames_folder_path_source
        else:
            file_source = labels_folder_path_source

        shutil.move(file_source + "\\" + file_name, path_destination)




if __name__ == "__main__":
    directory_images = frames_folder_path_source 
    directory_labels = labels_folder_path_source

    frames = os.listdir(directory_images)
    labels = os.listdir(directory_labels)

    dataset = np.array([[frames[i], labels[i]] for i in range(len(frames))])
    np.random.shuffle(dataset)

    frames = np.array([dataset[i][0] for i in range(len(dataset))])
    labels = np.array([dataset[i][1] for i in range(len(dataset))])
    
    frames_train, frames_test, labels_train, labels_test = train_test_split(frames, labels, test_size = 0.1)
    frames_train, frames_val, labels_train, labels_val = train_test_split(frames_train, labels_train, test_size=0.2)

    save_dataset(frames_train, 'datasets\\dataset\\images\\train', frames=True)
    save_dataset(labels_train, 'datasets\\dataset\\labels\\train', frames=False)

    save_dataset(frames_val, 'datasets\\dataset\\images\\val', frames=True)
    save_dataset(labels_val, 'datasets\\dataset\\labels\\val', frames=False)

    save_dataset(frames_test, 'datasets\\dataset\\images\\test', frames=True)
    save_dataset(labels_test, 'datasets\\dataset\\labels\\test', frames=False)