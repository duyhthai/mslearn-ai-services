using NUnit.Framework;
using System;

[TestFixture]
public class ProgramTests
{
    [Test]
    public void GetLanguage_WithEmptyString_ReturnsUndefined()
    {
        string AISvcKey = "your_key_here";
        string AISvcEndpoint = "your_endpoint_here";

        string result = Program.GetLanguage("");

        Assert.AreEqual("Undefined", result);
    }

    [Test]
    public void GetLanguage_WithSingleWord_ReturnsEnglish()
    {
        string AISvcKey = "your_key_here";
        string AISvcEndpoint = "your_endpoint_here";

        string result = Program.GetLanguage("Hello");

        Assert.AreEqual("English", result);
    }

    [Test]
    public void GetLanguage_WithMultipleWords_ReturnsCorrectLanguage()
    {
        string AISvcKey = "your_key_here";
        string AISvcEndpoint = "your_endpoint_here";

        string result = Program.GetLanguage("Bonjour le monde");

        Assert.AreEqual("French", result);
    }
}