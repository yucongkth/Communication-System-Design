
# Distributed Monitoring as a Service for SDN
Current SDN lacks monitoring capabilities like gathering packet and byte counters from the dataplane and QoS metrics, which is difficult for the system to achieve adaptive routing and admission control.

This project aims to collect information from data plane and then use the information to design an admission control and routing algorithm that can reconfigure an software-defined network to achieve full utilization under heavy load. Finally, we will evaluate different components in our system and show effectiveness of our system and reaction in different scenarios. [1]

This project will be divided into several parts:

I. Setup Testbed

The first task is setting up a monitoring system. We will use Mininet network emulator to implement the required topology. Then we will analyze where to plece the four zones so that we will have more paths between two zones and can achieve full utilization of the network.

II. Setup Basic Monitoring and Database

We will implement NFM and DM modules to collect data from the dataplane. The data will be stored in DM(we tend to use MySQL) analyze the statistics and finally plot average of total link utilization as well as packet drops while running a SDN applications(the SDN controller we choose is Ryu).

III. Implementing basic features in CPM

CPM should use different metrics to decide which paths should be used to establish new connections. We will also build up the evaluation strategy to show the functionality of CPM.

IV. Advanced Features in CPM

RPM will be implemented and its data will be used in path selection algorithm of CPM. Finally, admission control feature will be added to extend CPM.

V. Wrap-up

The group member will work together to complete the report and describe all the details of the project and implementation. Lastly, we will make a video to demonstrate our result and deliver a presentation at final workshop.

Team Members

Jiani Jiang jianij@kth.se, TCOMM

Yucong Zhang yucong@kth.se, TCOMM

Shimin Huang shimin@kth.se, TCOMM

Xinkai Xiong xinkaix@kth.se, TCOMM

Jiacheng Zheng jzhe@kth.se, TCOMM

References

[1] A. Farshin, "Project-1-SDN", https://kth.instructure.com/courses/6436/files/1191304?module_item_id=88164
