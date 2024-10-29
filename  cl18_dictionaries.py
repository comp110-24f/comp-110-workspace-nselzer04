"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

for key in ice_cream:
    print(ice_cream[key])

print(len(ice_cream))  # prints 3
# len evaluates to the numb of entries

ice_cream["mint"] = 3
# add key-value entry by directly assigning to a key


print(ice_cream["chocolate"])  # prints 12
# access entries by their key

has_pbj: bool = "pbj" in ice_cream
# test if "pbj" is a key in ice cream

ice_cream.pop("strawberry")
# to remove, we use the pop method and give a key

for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f" {flavor} has {tally} orders.")
