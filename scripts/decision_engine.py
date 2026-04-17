import hashlib
import json

def hash_data(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

def commit_pre(input_data):
    return {
        "input_hash": hash_data(input_data)
    }

def decision(input_data):
    return {
        "decision": "approve" if input_data["score"] > 0.5 else "reject"
    }

def create_trace(input_data):
    pre = commit_pre(input_data)
    result = decision(input_data)

    trace = {
        "pre": pre,
        "result": result
    }

    trace["trace_hash"] = hash_data(trace)
    return trace

if __name__ == "__main__":
    sample = {"score": 0.7}
    trace = create_trace(sample)

    print(json.dumps(trace, indent=2))
