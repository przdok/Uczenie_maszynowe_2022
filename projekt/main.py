import data_loader
import train_model
import evaluate

def main(data_path):
    (X_train, y_train), (X_test, y_test) = data_loader.load_and_preprocess_data(data_path)
    model = train_model.create_and_train_model(X_train, y_train, X_test, y_test)
    evaluate.evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main('C:\\Users\\Dell\\Downloads\\archive')