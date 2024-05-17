import rclpy
from std_msgs.msg import String
import argparse
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen



class mover_tartaruga(Node):

    def __init__(self):
        super().__init__('mover_tartaruga')

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.cli
        self.spawn_turtle

    def cli():
        parser = argparse.ArgumentParser()
        parser.add_argument("vx")
        parser.add_argument("vy")
        parser.add_argument("vtheta")
        parser.add_argument("tempo")
        parser.parse_args()
        global args 
        args = parser.parse_args()
        print("pode mandar ver")

    def spawn_turtle(self):
        spawn_client = self.create_client(Spawn, 'spawn')
        while not spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Serviço "spawn" não disponível, esperando...')

        request = Spawn.Request()
        request.x = float(args.vx)
        request.y = float(args.vy)
        request.theta = float(arg.theta)

def main(args=None):
    rclpy.init(args=args)

    mover_tartaruga= mover_tartaruga()

    rclpy.spin(mover_tartaruga)

    mover_tartaruga.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()