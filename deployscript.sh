#shell variables
home=/opt/apps/tomcat8
START=$home/bin/startup.sh
SHUTDOWN=$home/bin/shutdown.sh
SRCDIR=$home/webapps/roshambo*
DESDIR=/opt/apps/files

PID=$home/bin/CATALINA_PID
#SRC=$home/webapps/rps.war

FILENAME=rps-$(date +"%Y-%m-%d-%H.%M.%S").tar.gz

echo "shutdown tomcat"
$SHUTDOWN

echo "backup existing war file"
tar -czvf $DESDIR/$FILENAME $SRCDIR
echo "backup finished"

echo "delete war file"
rm -rf $home/webapps/roshambo*

echo "move war to webapps"
cp -r  /var/lib/jenkins/workspace/SampleJob/target/roshambo*  $home/webapps

echo "start tomcat"
$START
