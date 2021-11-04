IMAGE_LIST = [
    "https://moderatorsampleimages.blob.core.windows.net/samples/sample2.jpg",
    "https://moderatorsampleimages.blob.core.windows.net/samples/sample5.png"
]

for image_url in IMAGE_LIST:
    print("\nEvaluate image {}".format(image_url))

print("\nEvaluate for adult and racy content.")
evaluation = client.image_moderation.evaluate_url_input(
    content_type="application/json",
    cache_image=True,
    data_representation="URL",
    value=image_url
)
assert isinstance(evaluation, Evaluate)
pprint(evaluation.as_dict())