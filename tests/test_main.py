#!/usr/bin/env python3

import sys
from unittest import mock

import pytest

from dryml import main
from tests.helpers_tests import run_dryml_cli


def test_help_text(monkeypatch, capsys):
    # When
    mock_exit = mock.Mock(side_effect=ValueError("raised in test to exit early"))
    with mock.patch.object(sys, "exit", mock_exit), pytest.raises(
            ValueError, match="raised in test to exit early"
    ):
        assert not run_dryml_cli(["--help"])
    # Then
    captured = capsys.readouterr()
    assert "usage: dryml" in captured.out


def test_version(monkeypatch, capsys):
    # When
    mock_exit = mock.Mock(side_effect=ValueError("raised in test to exit early"))
    with mock.patch.object(sys, "exit", mock_exit), pytest.raises(
            ValueError, match="raised in test to exit early"
    ):
        assert not run_dryml_cli(["--version"])
    # Then
    captured = capsys.readouterr()
    mock_exit.assert_called_with(0)
    assert main.__version__ in captured.out.strip()
