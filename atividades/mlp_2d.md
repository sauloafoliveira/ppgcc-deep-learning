


![logo](../ppgc_logo.png)

---

Aprendizagem Profunda – 2025.1

**Prof. Dr. Saulo Oliveira**

Data de Entrega: Uma semana após a definição.

Meio de Entrega: ```Colab com simulações```.

---

## PARTE A. Rede Perceptron de Múltiplas Camadas

1. Baixe a versão dos conjuntos de dados que eu usei na minha Tese: ```load_banana```, ```load_ripley``` e ```load_two_moon```. Comece pelo Two moons.
   
2. Divida de forma aleatória o conjunto entre treino (80%) e teste (20%).
   
   -  Normalize os dados com a estratégia média e desvio padrão somente pelos
dados de treino;   
   - Treine uma rede MLP com até cinco camada ocultas, com até quinze neurônios cada;   
   - Plote a superfície de decisão da MLP, veja o seaborn, use o GePeTo;   
   - Mostre a Matriz de Confusão;
   - Rode a função ```inspect_model``` para tirarmos as medidas de desempenho necessárias.

1. Repita os passos anteriores para as bases de dados Ripley e Banana.
**OBS**: O código abaixo está incompleto.

## Exemplo de uso

```python
# Baixem do meu github
!mkdir -p local_datasets
!wget --quiet 'https://raw.githubusercontent.com/sauloafoliveira/cclw-mlm/master/local_datasets/__init__.py' -O 'local_datasets/__init__.py'
!wget --quiet 'https://raw.githubusercontent.com/sauloafoliveira/cclw-mlm/master/local_datasets/datasets-7627-10826-banana.csv' -O 'local_datasets/datasets-7627-10826-banana.csv'
!wget --quiet 'https://raw.githubusercontent.com/sauloafoliveira/cclw-mlm/master/local_datasets/rip.csv' -O 'local_datasets/rip.csv'


# importem o código assim
from sklearn.model_selection import train_test_split
from local_datasets import load_banana, load_ripley, load_two_moon
import torch
from torch.utils.data import TensorDataset, DataLoader

bunch = load_ripley()
X, y = bunch.data, bunch.target
print(X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y  # estratifica para manter proporção de classes
)

# Converte para tensores do PyTorch
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32)
X_test_tensor  = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor  = torch.tensor(y_test, dtype=torch.float32)

# Datasets e DataLoaders
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader  = DataLoader(test_dataset, batch_size=32, shuffle=False)

```


# Para avaliar o desempenho, utilizem a função que segue:
```python
from collections import Counter
import torch

def count_module_types(model):
    module_types = [type(m).__name__ for m in model.modules() if not isinstance(m, torch.nn.Sequential)]
    return Counter(module_types)

def count_trainable_params(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def evaluate_model(model, dataloader, device='cpu'):
    model.eval()
    correct, total, loss_total = 0, 0, 0.0
    criterion = torch.nn.BCELoss()

    with torch.no_grad():
        for x, y in dataloader:
            x, y = x.to(device), y.to(device).float().view(-1, 1)  # reshape y to match output
            output = model(x)
            loss = criterion(output, y)
            loss_total += loss.item()

            # Para acurácia: saída > 0.5 -> classe 1
            predicted = (output >= 0.5).float()
            total += y.size(0)
            correct += (predicted == y).sum().item()
    accuracy = 100 * correct / total
    avg_loss = loss_total / len(dataloader)
    return accuracy, avg_loss

def inspect_model(model, dataloader, device='cpu'):
    
    num_params = count_trainable_params(model)
    modules_used = count_module_types(model)
    accuracy, loss = evaluate_model(model, dataloader, device)


    print(f"✅ Total trainable parameters: {num_params}")
    print(f"📦 Modules: {modules_used.total()}")
    print(f"🎯 Accuracy: {accuracy:.2f}%")
    print(f"📉 Average loss: {loss:.4f}\n")

    return {
        'parameters': num_params,
        'modules': modules_used.total(),
        'accuracy': round(accuracy, 2),
        'loss': round(loss, 3)
    }
```

# O baseline de vocês é meu modelo.
```python
mlp = torch.nn.Sequential(
    torch.nn.Linear(2, 1),
    torch.nn.Sigmoid()
)

inspect_model(mlp, train_dataloader)
```

✅ Total trainable parameters: 3
📦 Modules: 2
🎯 Accuracy: 49.87%
📉 Average loss: 0.6815

