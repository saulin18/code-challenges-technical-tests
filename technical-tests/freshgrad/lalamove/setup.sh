#!/bin/bash

# Verify if the file exists at /data/orders.json

[ -d ./data ] || mkdir -p ./data

# Verify if the file is empty
[ -f ./data/orders.json ] || echo "[]" > ./data/orders.json

# Try to compile the Python file and run the executable

echo "Compiling Python file and running executable"

echo '#!/bin/bash' > llm
echo 'python3 src/main.py "$@"' >> llm

# Run the executable
chmod +x ./llm

export PATH="$PATH:$(pwd)"


echo ""
echo "To use 'llm' without './', run:"
echo "export PATH=\"\$PATH:$(pwd)\""
echo ""
echo "Or add this line to your ~/.bashrc:"
echo "export PATH=\"\$PATH:$(pwd)\""

