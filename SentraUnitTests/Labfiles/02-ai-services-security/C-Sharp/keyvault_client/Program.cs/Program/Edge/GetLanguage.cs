using NUnit.Framework;
using System;

[TestFixture]
public class ProgramTests
{
    private const string aiSvcKey = "your-key-here";
    private const string aiSvcEndpoint = "your-endpoint-here";

    [Test]
    public void GetLanguage_EmptyText_ReturnsEmptyString()
    {
        string result = Program.GetLanguage("");
        Assert.IsEmpty(result);
    }

    [Test]
    public void GetLanguage_SingleWordEnglish_ReturnsEnglish()
    {
        string result = Program.GetLanguage("Hello");
        Assert.AreEqual("English", result);
    }

    [Test]
    public void GetLanguage_ComplexSentenceSpanish_ReturnsSpanish()
    {
        string result = Program.GetLanguage("¿Cómo estás?");
        Assert.AreEqual("Spanish", result);
    }
}