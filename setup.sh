#!/bin/bash

case $1 in
	"start")
		name=$( whoami )
		currentPath=$( pwd )
		echo -e "启动服务：\n当前用户：${name} \n当前目录：${currentPath}"
		;;
	"stop")
		echo "终止服务"
		;;
	"reload")
		echo "重启服务"
		;;
	*)
		echo "Usage [start|stop|reload]"
esac