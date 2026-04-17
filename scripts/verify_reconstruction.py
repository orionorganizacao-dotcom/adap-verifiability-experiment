import json
import hashlib


def hash_data(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def verify_trace(input_path, trace_path):
    input_data = load_json(input_path)
    trace = load_json(trace_path)

    expected_input_hash = hash_data(input_data)
    actual_input_hash = trace["pre"]["input_hash"]

    recomputed_trace = {
        "pre": trace["pre"],
        "result": trace["result"]
    }
    expected_trace_hash = hash_data(recomputed_trace)
    actual_trace_hash = trace["trace_hash"]

    return {
        "input_hash_match": expected_input_hash == actual_input_hash,
        "trace_hash_match": expected_trace_hash == actual_trace_hash,
        "decision": trace["result"]["decision"]
    }


if __name__ == "__main__":
    result = verify_trace("data/input.json", "logs/verifiable_trace.json")
    print(json.dumps(result, indent=2))
