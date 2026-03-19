"""Tests for device agent JSON parsing and validation."""

import pytest

from device_prediction.device_agent import DeviceFeatures, parse_device_response


class TestParseDeviceResponse:
    def test_clean_json(self):
        raw = '{"device_name": "IPHONE 16", "manufacturer": "APPLE", "release_year": 2024, "ram_gb": 8, "storage_base_gb": 128, "display_type": "OLED", "display_size_inches": 6.1, "camera_rear_mp": 48, "camera_front_mp": 12, "launch_price_nok": 11990, "device_series_annual": "Flagship", "device_series_annual_no": 5, "generation": "16", "context_summary": "Standard flagship"}'
        result = parse_device_response(raw, "APPLE IPHONE 16")
        assert result.device_name == "IPHONE 16"
        assert result.manufacturer == "APPLE"
        assert result.user_input == "APPLE IPHONE 16"
        assert result.ram_gb == 8.0

    def test_markdown_fenced_json(self):
        raw = """Here is the data:
```json
{"device_name": "GALAXY S24", "manufacturer": "SAMSUNG", "release_year": 2024, "ram_gb": 8}
```
"""
        result = parse_device_response(raw, "SAMSUNG GALAXY S24")
        assert result.device_name == "GALAXY S24"
        assert result.manufacturer == "SAMSUNG"

    def test_trailing_comma_fixed(self):
        raw = '{"device_name": "PIXEL 8", "manufacturer": "GOOGLE", "ram_gb": 8,}'
        result = parse_device_response(raw, "GOOGLE PIXEL 8")
        assert result.device_name == "PIXEL 8"

    def test_nested_features_flattened(self):
        raw = '{"device_name": "XPERIA 5", "manufacturer": "SONY", "features": {"ram_gb": 6, "storage_base_gb": 128}}'
        result = parse_device_response(raw, "SONY XPERIA 5")
        assert result.ram_gb == 6.0
        assert result.storage_base_gb == 128.0

    def test_user_input_forced(self):
        raw = '{"device_name": "IPHONE 15", "manufacturer": "APPLE", "user_input": "wrong value"}'
        result = parse_device_response(raw, "APPLE IPHONE 15")
        assert result.user_input == "APPLE IPHONE 15"

    def test_invalid_json_raises(self):
        raw = "This is not JSON at all"
        with pytest.raises(Exception):
            parse_device_response(raw, "UNKNOWN DEVICE")

    def test_numeric_coercion(self):
        raw = '{"device_name": "TEST", "manufacturer": "TEST", "launch_price_nok": "12 500", "ram_gb": "8"}'
        result = parse_device_response(raw, "TEST TEST")
        assert result.launch_price_nok == 12500.0
        assert result.ram_gb == 8.0


class TestDeviceFeaturesModel:
    def test_uppercase_enforcement(self):
        f = DeviceFeatures(
            user_input="apple iphone 16",
            device_name="iphone 16",
            manufacturer="apple",
        )
        assert f.device_name == "IPHONE 16"
        assert f.manufacturer == "APPLE"

    def test_optional_fields_default_none(self):
        f = DeviceFeatures(
            user_input="TEST",
            device_name="TEST",
            manufacturer="TEST",
        )
        assert f.ram_gb is None
        assert f.launch_price_nok is None
        assert f.context_summary is None
