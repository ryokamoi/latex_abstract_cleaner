# Abstract Conversion Tool

A Python utility for converting LaTeX abstracts to clean, readable text format for academic paper submissions to arXiv and OpenReview. The tool removes LaTeX commands, comments, and applies custom replacements to ensure your abstract displays correctly on these platforms.

## Why This Tool?

Academic paper submission platforms like arXiv and OpenReview require plain text abstracts, but many researchers write their abstracts in LaTeX with:
- Custom macros for method names (`\ourmethod{}`)
- Dataset name shortcuts (`\dataset{}`)
- LaTeX formatting commands
- Comments and collaborative annotations

This tool automatically converts your LaTeX abstract to clean, submission-ready text while preserving the intended meaning and formatting.

## Requirements

- Python 3.x

## Usage

1. Place your LaTeX abstract in `original.txt`
2. Configure project-specific replacements in `replace_list.csv` (optional)
3. Run the script:
   ```bash
   python convert_abstract.py
   ```
4. Copy the converted text from `converted.txt` to your arXiv or OpenReview submission form

## Configuration

### Replace List (`replace_list.csv`)

Define custom text replacements in CSV format. This is particularly useful for converting LaTeX macros to their full names for academic submissions. Each line should contain two columns: the text to find and the text to replace it with. For example:

```csv
\visonlyqa,VisOnlyQA
\fover,FoVer
```

## License

Please see the [LICENSE](LICENSE) file for details.
