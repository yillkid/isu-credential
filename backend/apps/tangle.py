import json
from iota import Iota, ProposedTransaction, Address, TryteString, Tag, Transaction, ProposedBundle, Hash
from iota.trits import trits_from_int
from apps.config import SEED, DEPTH, MIN_WEIGHT_MAGNITUDE, NODE_URL

receiver_address = "ILXW9VMJQVFQVKVE9GUZSODEMIMGOJIJNFAX9PPJHYQPUHZLTWCJZKZKCZYKKJJRAKFCCNJN9EWOW9N9YDGZDDQDDC"
txn_tag = "TXNTAGS"
value = 0

def write_data_to_tangle(data):
    # Iota instance
    api = Iota(NODE_URL, SEED)

    # Txn description
    txn = ProposedTransaction(
        address = Address(receiver_address),
        message = TryteString.from_string(json.dumps(data)),
        tag = Tag(txn_tag),
        value = value,
        )

    # Send transaction
    prepared_transferes = []
    bundle = ""
    prepared_transferes.append(txn)
    try:
        bundle = api.send_transfer(
            depth = DEPTH,
            transfers = prepared_transferes,
            min_weight_magnitude = MIN_WEIGHT_MAGNITUDE
        )
    except Exception as e:
        print(e)
        return e

    print(bundle['bundle'].hash)
    return {"status":200, "bundle":bundle['bundle'].hash}
