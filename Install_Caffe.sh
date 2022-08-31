# Modify Makefile.config according to your Caffe installation.
# cp Makefile.config.example Makefile.config
cd caffe
make clean
make -j8
# Make sure to include $CAFFE_ROOT/python to your PYTHONPATH.
make py
make test -j8
# (Optional)
make runtest -j8

