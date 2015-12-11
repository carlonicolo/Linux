mkdir /usr/local/jvm/
tar -xvf /home/karlitos/Downloads/jdk-*.tar.gz
mv jdk1.8.* jdk1.8.0
mv jdk1.8.0 /usr/lib/jvm/

update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0/bin/java" 1
update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0/bin/javac" 1
update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/jvm/jdk1.8.0/bin/javaws" 1 

update-alternatives --config java
update-alternatives --config javac
update-alternatives --config javaws

echo "Fine script, verifico la versione della jdk \n"
java -version

echo "Ciao"
