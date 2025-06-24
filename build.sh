# clean up from preexisting
rm -rf bin

# Install lua (latest, update it when new stuff comes out)

mkdir bin
curl -L -R -O https://www.lua.org/ftp/lua-5.4.8.tar.gz
tar zxf lua-5.4.8.tar.gz
cd lua-5.4.8
make all test
cd src 
cp -r lua ../../bin/lua
cd ../..
# clean up
rm -rf lua-5.4.8
rm -rf lua-5.4.8.tar.gz

cd AI
mkdir data
cd generation
python gen.py
python remind.py
python time.py