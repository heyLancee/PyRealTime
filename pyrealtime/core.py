import time
import threading
from typing import Callable

class RealTimeSimulation:
    """
    实时仿真模块类
    """
    
    def __init__(self, sample_time: float):
        """
        初始化实时仿真实例
        
        Args:
            sample_time (float): 采样时间(秒)
        """
        self.sample_time = sample_time
        self.is_running = False
        self.current_time = 0.0
        self._simulation_thread = None
        self._stop_event = threading.Event()

    def _simulation_loop(self, callback: Callable[[float], None]):
        """
        仿真主循环
        
        Args:
            callback: 每个采样周期执行的回调函数
        """
        while not self._stop_event.is_set():
            loop_start_time = time.time()
            
            # 执行回调
            callback(self.current_time)
            self.current_time += self.sample_time
            
            # 计算需要等待的时间以保持采样周期
            elapsed_time = time.time() - loop_start_time
            sleep_time = max(0, self.sample_time - elapsed_time)
            time.sleep(sleep_time)

    def start(self, callback: Callable[[float], None]):
        """
        启动实时仿真
        
        Args:
            callback: 每个采样周期执行的回调函数，接收当前仿真时间作为参数
        """
        if self.is_running:
            return
        
        self.reset()
            
        self.is_running = True
        self._stop_event.clear()
        self._simulation_thread = threading.Thread(
            target=self._simulation_loop,
            args=(callback,),
            daemon=True
        )
        self._simulation_thread.start()

    def stop(self):
        """
        停止实时仿真
        """
        if not self.is_running:
            return
            
        self._stop_event.set()
        if self._simulation_thread:
            self._simulation_thread.join()
        self.is_running = False

    def reset(self):
        """
        重置仿真时间
        """
        self.current_time = 0.0

    def get_current_time(self) -> float:
        """
        获取当前仿真时间
        
        Returns:
            float: 当前仿真时间(秒)
        """
        return self.current_time 