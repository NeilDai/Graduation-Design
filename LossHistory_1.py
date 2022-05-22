from tensorflow import keras
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'

class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs=None):
        if logs is None:
            logs = {}
        self.losses = {'batch': [], 'epoch': []}
        self.accuracy = {'batch': [], 'epoch': []}


    def on_batch_end(self, batch, logs=None):
        if logs is None:
            logs = {}
        self.losses['batch'].append(logs.get('loss'))
        self.accuracy['batch'].append(logs.get('accuracy'))


    def on_epoch_end(self, batch, logs=None):
        if logs is None:
            logs = {}
        self.losses['epoch'].append(logs.get('loss'))
        self.accuracy['epoch'].append(logs.get('accuracy'))


    def loss_plot(self, loss_type):

        iters = range(len(self.losses[loss_type]))
        #创建一个图
        plt.figure()
        # acc
        acc = plt.plot(iters, self.accuracy[loss_type], 'r', label='train accuracy')
        # loss
        loss = plt.plot(iters, self.losses[loss_type], 'g', label='train loss')
        plt.grid(True)#设置网格形式
        plt.xlabel(loss_type)
        plt.ylabel('accuracy-loss')#给x，y轴加注释
        plt.title('Accuracy-Loss curve for CNN -consensus 独热编码')
        plt.legend(loc="upper right")#设置图例显示位置
        plt.show()

if __name__ == '__main__':
    main()
