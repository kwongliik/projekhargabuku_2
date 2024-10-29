import pytest
from harga_buku import harga_bayaran  # Replace `your_module` with the actual module name where the function is defined

@pytest.mark.parametrize("jenisbuku, kuantiti, expected_potongan_harga, expected_harga", [
    (1, 10, (6.00 * 0.1) * 10, (6.00 * 10) - ((6.00 * 0.1) * 10)),  # Test for book type 1
    (2, 5, (7.50 * 0.08) * 5, (7.50 * 5) - ((7.50 * 0.08) * 5)),   # Test for book type 2
    (3, 8, (8.90 * 0.05) * 8, (8.90 * 8) - ((8.90 * 0.05) * 8)),   # Test for book type 3 (other types)
    (1, 0, 0.0, 0.0),  # Edge case: quantity = 0, book type 1
    (2, 0, 0.0, 0.0),  # Edge case: quantity = 0, book type 2
    (3, 0, 0.0, 0.0),  # Edge case: quantity = 0, other book types
])
def test_harga_bayaran(jenisbuku, kuantiti, expected_potongan_harga, expected_harga):
    assert harga_bayaran(jenisbuku, kuantiti) == (expected_potongan_harga, expected_harga)
