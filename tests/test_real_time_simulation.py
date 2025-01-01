import time
from PyRealTime import RealTimeSimulation

def simulation_callback(time):
    print(f"当前仿真时间: {time:.2f}秒")

if __name__ == '__main__':
    # 创建仿真实例，采样时间为0.1秒
    simulation = RealTimeSimulation(sample_time=0.1)

    # 启动仿真
    simulation.start(simulation_callback)

    # 运行5秒后停止
    time.sleep(5)
    simulation.stop()

    time.sleep(1)
    print("仿真结束")
