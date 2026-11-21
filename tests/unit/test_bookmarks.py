from readly_mcp.server import bookmarks_op


def test_add_list_remove(tmp_path, monkeypatch):
    monkeypatch.setenv("READLY_BOOKMARKS_FILE", str(tmp_path / "b.json"))
    assert bookmarks_op("add", "https://x/1", "A")["success"]
    assert bookmarks_op("add", "https://x/1", "A2")["success"]  # dedupes
    items = bookmarks_op("list")["bookmarks"]
    assert [b["title"] for b in items] == ["A2"]
    assert bookmarks_op("remove", "https://x/1")["success"]
    assert not bookmarks_op("remove", "https://x/1")["success"]
    assert not bookmarks_op("add")["success"]
    assert not bookmarks_op("nope")["success"]
