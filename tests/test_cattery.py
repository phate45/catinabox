import pytest

from catinabox import cattery, mccattery


@pytest.fixture(params=[
    cattery.Cattery,
    mccattery.McCattery
])
def cattery_client(request):
    return request.param()


###########################################################################
# add_cats
###########################################################################

def test__add_cats__succeeds(cattery_client):
    c = cattery_client
    c.add_cats(["Fluffy", "Snookums"])
    assert c.cats == ["Fluffy", "Snookums"]
    assert c.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(cattery_client):
    c = cattery_client
    c.add_cats(["Fluffy", "Junior"])
    c.remove_cat("Fluffy")
    assert c.cats == ["Junior"]
    assert c.num_cats == 1


def test__remove_cat__no_cats__fails(cattery_client):
    c = cattery_client
    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(cattery_client):
    c = cattery_client
    c.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("Snookums")


###########################################################################
# history
###########################################################################

def test__history_empty_on_init():
    c = mccattery.McCattery()
    assert len(c.history) == 0


def test__history_has_expected_length():
    cats_to_add = ["Fluffy"]
    c = mccattery.McCattery()

    c.add_cats(cats_to_add)

    assert len(c.history) == len(cats_to_add)


def test__history_records_removal():
    cats_to_add = ["Fluffy"]
    c = mccattery.McCattery()

    c.add_cats(cats_to_add)
    c.remove_cat(cats_to_add[0])

    # two operations ought to be recorded
    assert len(c.history) == 2
