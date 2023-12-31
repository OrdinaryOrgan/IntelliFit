# Readme

## IntelliFit: Your Smart AIoT Fitness Companian

### How to use
- Overview
> This is an AIoT Project, which means you need some AI and IoT.
> The IoT part is mainly about Raspberry Pi, so you may need one type of it.
> The AI part uses a pre-trained model, you can train it if you want.

- Backend and Frontend  
> This is a SpringBoot Application, start the backend in *`AIOTProjectApplication.java`*  
> After starting the SpringBoot Application, using your web browser to view the User Interface at <https://localhost/>

- MQTT Subscriber
> MQTT Subscriber runs on the client, so you may run it on your PC.
> Start to subscribe data from publisher in `/Client/Conn/DataSubscribe.py`  
> Type `python /Client/Conn/DataSubscribe.py` and run in Command line

- Raspberry Pi
> Start to process and publish data in `/Pi/StartPublish.py`
> Type `python /Pi/StartPublish.py` and run in Command line

### Other Tips
- Please check the `/Client/pow.xml` and `/Client/src/main/resources/application.yml` to learn about configuration
- Configuration of database also appear in `/Client/Conn/DataSubscribe.py`

### Copyright and Thank
- Our team from XJTU & SCU copyrights this project, and I only copyright the **Backend** and **Database** part.
- Thank my teammates for authorizing me to publish our projects on my GitHub account.