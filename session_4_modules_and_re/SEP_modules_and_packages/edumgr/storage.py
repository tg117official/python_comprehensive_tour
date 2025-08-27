# Text & pickle I/O with try/except/else/finally
import pickle

def write_text(path, text):
    f = None
    try:
        f = open(path, "w", encoding="utf-8")
        f.write(text)
    except OSError as e:
        print("Text write error:", e)
    else:
        print(f"Saved text report -> {path}")
    finally:
        if f is not None:
            f.close()

def load_gradebook(path):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print("Gradebook load error:", e)
        return {}

def save_gradebook(path, data):
    pf = None
    try:
        pf = open(path, "wb")
        pickle.dump(data, pf, protocol=pickle.HIGHEST_PROTOCOL)
    except OSError as e:
        print("Pickle save error:", e)
    else:
        print(f"Gradebook updated -> {path}  (students: {len(data)})")
    finally:
        if pf is not None:
            pf.close()
