from temper_std.testing import Test
from unittest import TestCase as TestCase25
from builtins import str as str13, bool as bool15
from typing import Sequence as Sequence14
from ormery.html import html_codec, str_cat_5804, SafeHtmlBuilder, SafeHtml, list_for_each_5815
class TestCase47(TestCase25):
    def test___htmlDecoding__804(self) -> None:
        'HTML decoding'
        test_9: Test = Test()
        try:
            actual_805: 'str13' = html_codec.decode('')
            t_5597: 'bool15' = actual_805 == ''
            def fn_5594() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("") == (', '', ') not (', actual_805, ')')
            test_9.assert_(t_5597, fn_5594)
            actual_807: 'str13' = html_codec.decode('&l')
            t_5601: 'bool15' = actual_807 == '&l'
            def fn_5593() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&l") == (', '&l', ') not (', actual_807, ')')
            test_9.assert_(t_5601, fn_5593)
            actual_809: 'str13' = html_codec.decode('&lt')
            t_5605: 'bool15' = actual_809 == '<'
            def fn_5592() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&lt") == (', '<', ') not (', actual_809, ')')
            test_9.assert_(t_5605, fn_5592)
            actual_811: 'str13' = html_codec.decode('&lt;')
            t_5609: 'bool15' = actual_811 == '<'
            def fn_5591() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&lt;") == (', '<', ') not (', actual_811, ')')
            test_9.assert_(t_5609, fn_5591)
            actual_813: 'str13' = html_codec.decode('&Bcy;')
            t_5613: 'bool15' = actual_813 == '\u0411'
            def fn_5590() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&Bcy;") == (', '\u0411', ') not (', actual_813, ')')
            test_9.assert_(t_5613, fn_5590)
            actual_815: 'str13' = html_codec.decode('&Bcy')
            t_5617: 'bool15' = actual_815 == '&Bcy'
            def fn_5589() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&Bcy") == (', '&Bcy', ') not (', actual_815, ')')
            test_9.assert_(t_5617, fn_5589)
            actual_817: 'str13' = html_codec.decode('&LT;')
            t_5621: 'bool15' = actual_817 == '<'
            def fn_5588() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&LT;") == (', '<', ') not (', actual_817, ')')
            test_9.assert_(t_5621, fn_5588)
            actual_819: 'str13' = html_codec.decode('&Aacute;')
            t_5625: 'bool15' = actual_819 == '\xc1'
            def fn_5587() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&Aacute;") == (', '\xc1', ') not (', actual_819, ')')
            test_9.assert_(t_5625, fn_5587)
            actual_821: 'str13' = html_codec.decode('&aacute;')
            t_5629: 'bool15' = actual_821 == '\xe1'
            def fn_5586() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&aacute;") == (', '\xe1', ') not (', actual_821, ')')
            test_9.assert_(t_5629, fn_5586)
            actual_823: 'str13' = html_codec.decode('&AaCuTe;')
            t_5633: 'bool15' = actual_823 == '&AaCuTe;'
            def fn_5585() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&AaCuTe;") == (', '&AaCuTe;', ') not (', actual_823, ')')
            test_9.assert_(t_5633, fn_5585)
            actual_825: 'str13' = html_codec.decode('&gt;;')
            t_5637: 'bool15' = actual_825 == '>;'
            def fn_5584() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&gt;;") == (', '>;', ') not (', actual_825, ')')
            test_9.assert_(t_5637, fn_5584)
            actual_827: 'str13' = html_codec.decode('&amp;lt;')
            t_5641: 'bool15' = actual_827 == '&lt;'
            def fn_5583() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.decode("&amp;lt;") == (', '&lt;', ') not (', actual_827, ')')
            test_9.assert_(t_5641, fn_5583)
        finally:
            test_9.soft_fail_to_hard()
class TestCase48(TestCase25):
    def test___htmlEncoding__829(self) -> None:
        'HTML encoding'
        test_10: Test = Test()
        try:
            actual_830: 'str13' = html_codec.encode('')
            t_5573: 'bool15' = actual_830 == ''
            def fn_5570() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.encode("") == (', '', ') not (', actual_830, ')')
            test_10.assert_(t_5573, fn_5570)
            actual_832: 'str13' = html_codec.encode('Hello, World!')
            t_5577: 'bool15' = actual_832 == 'Hello, World!'
            def fn_5569() -> 'str13':
                return str_cat_5804('expected `-work/src//html/`.htmlCodec.encode("Hello, World!") == (', 'Hello, World!', ') not (', actual_832, ')')
            test_10.assert_(t_5577, fn_5569)
            actual_834: 'str13' = html_codec.encode("<foo> & <bar baz='b\"oo'> far")
            t_5581: 'bool15' = actual_834 == '&lt;foo&gt; &amp; &lt;bar baz=&#39;b&#34;oo&#39;&gt; far'
            def fn_5568() -> 'str13':
                return str_cat_5804("expected `-work/src//html/`.htmlCodec.encode(\"<foo> & <bar baz='b\\\"oo'> far\") == (", '&lt;foo&gt; &amp; &lt;bar baz=&#39;b&#34;oo&#39;&gt; far', ') not (', actual_834, ')')
            test_10.assert_(t_5581, fn_5568)
        finally:
            test_10.soft_fail_to_hard()
class TestCase50(TestCase25):
    def test___helloWorldHtmlStyle__899(self) -> None:
        'hello world, html style'
        test_32: Test = Test()
        try:
            t_4675: 'SafeHtmlBuilder' = SafeHtmlBuilder()
            t_4675.append_safe('Hello, <b>')
            t_4675.append_string('World')
            t_4675.append_safe('</b>!')
            actual_900: 'str13' = t_4675.accumulated.to_string()
            t_4682: 'bool15' = actual_900 == 'Hello, <b>World</b>!'
            def fn_4674() -> 'str13':
                return str_cat_5804('expected stringExpr(`-work/src//html/`.html, true, "Hello, <b>", \\interpolate, "World", "</b>!").toString() == (', 'Hello, <b>World</b>!', ') not (', actual_900, ')')
            test_32.assert_(t_4682, fn_4674)
        finally:
            test_32.soft_fail_to_hard()
class TestCase51(TestCase25):
    def test___autoescaped__903(self) -> None:
        'autoescaped'
        test_33: Test = Test()
        try:
            t_4665: 'SafeHtmlBuilder' = SafeHtmlBuilder()
            t_4665.append_safe('1 + 1 ')
            t_4665.append_string('<')
            t_4665.append_safe(' 3.')
            actual_904: 'str13' = t_4665.accumulated.to_string()
            t_4672: 'bool15' = actual_904 == '1 + 1 &lt; 3.'
            def fn_4664() -> 'str13':
                return str_cat_5804('expected stringExpr(`-work/src//html/`.html, true, "1 + 1 ", \\interpolate, "<", " 3.").toString() == (', '1 + 1 &lt; 3.', ') not (', actual_904, ')')
            test_33.assert_(t_4672, fn_4664)
        finally:
            test_33.soft_fail_to_hard()
class TestCase52(TestCase25):
    def test___contextMattersUrlsEmbed__907(self) -> None:
        'context matters -- URLs embed'
        test_34: Test = Test()
        try:
            def ok_url_483() -> 'str13':
                return "https://example.com/isn't-a-problem"
            def evil_url_484() -> 'str13':
                return "javascript:alert('evil done')"
            t_4642: 'SafeHtmlBuilder' = SafeHtmlBuilder()
            t_4642.append_safe("<a href='")
            t_4642.append_string("https://example.com/isn't-a-problem")
            t_4642.append_safe("'>")
            t_4642.append_string("https://example.com/isn't-a-problem")
            t_4642.append_safe('</a>')
            actual_908: 'str13' = t_4642.accumulated.to_string()
            t_4651: 'bool15' = actual_908 == "<a href='https://example.com/isn&#39;t-a-problem'>https://example.com/isn&#39;t-a-problem</a>"
            def fn_4641() -> 'str13':
                return str_cat_5804("expected stringExpr(`-work/src//html/`.html, true, \"<a href='\", \\interpolate, okUrl(), \"'>\", \\interpolate, okUrl(), \"</a>\").toString() == (", "<a href='https://example.com/isn&#39;t-a-problem'>https://example.com/isn&#39;t-a-problem</a>", ') not (', actual_908, ')')
            test_34.assert_(t_4651, fn_4641)
            t_4653: 'SafeHtmlBuilder' = SafeHtmlBuilder()
            t_4653.append_safe("<a href='")
            t_4653.append_string("javascript:alert('evil done')")
            t_4653.append_safe("'>")
            t_4653.append_string("javascript:alert('evil done')")
            t_4653.append_safe('</a>')
            actual_911: 'str13' = t_4653.accumulated.to_string()
            t_4662: 'bool15' = actual_911 == "<a href='about:zz_Temper_zz#'>javascript:alert(&#39;evil done&#39;)</a>"
            def fn_4640() -> 'str13':
                return str_cat_5804("expected stringExpr(`-work/src//html/`.html, true, \"<a href='\", \\interpolate, evilUrl(), \"'>\", \\interpolate, evilUrl(), \"</a>\").toString() == (", "<a href='about:zz_Temper_zz#'>javascript:alert(&#39;evil done&#39;)</a>", ') not (', actual_911, ')')
            test_34.assert_(t_4662, fn_4640)
        finally:
            test_34.soft_fail_to_hard()
class TestCase53(TestCase25):
    def test___quoteAdjustments__914(self) -> None:
        'quote adjustments'
        test_35: Test = Test()
        try:
            class_name_488: 'str13' = 'some-class'
            t_4629: 'SafeHtmlBuilder' = SafeHtmlBuilder()
            t_4629.append_safe('<hr class=')
            t_4629.append_string('some-class')
            t_4629.append_safe("><hr class='")
            t_4629.append_string('some-class')
            t_4629.append_safe("'><hr class=other-class>")
            actual_915: 'str13' = t_4629.accumulated.to_string()
            t_4638: 'bool15' = actual_915 == "<hr class=\"some-class\"><hr class='some-class'><hr class=\"other-class\">"
            def fn_4628() -> 'str13':
                return str_cat_5804("expected stringExpr(`-work/src//html/`.html, true, \"<hr class=\", \\interpolate, className, \"><hr class='\", \\interpolate, className, \"'><hr class=other-class>\").toString() == (", "<hr class=\"some-class\"><hr class='some-class'><hr class=\"other-class\">", ') not (', actual_915, ')')
            test_35.assert_(t_4638, fn_4628)
        finally:
            test_35.soft_fail_to_hard()
class TestCase54(TestCase25):
    def test___safehtmlInjectedInTagAndAttributeContext__918(self) -> None:
        'safehtml injected in tag and attribute context'
        test_36: Test = Test()
        try:
            t_4614: 'SafeHtmlBuilder' = SafeHtmlBuilder()
            t_4614.append_safe('I <3 <b>Ponies</b>!')
            love_490: 'SafeHtml' = t_4614.accumulated
            t_4617: 'SafeHtmlBuilder' = SafeHtmlBuilder()
            t_4617.append_safe('<b>')
            t_4617.append_safe_html(love_490)
            t_4617.append_safe("</b><img alt='")
            t_4617.append_safe_html(love_490)
            t_4617.append_safe("' src='ponies'>")
            actual_920: 'str13' = t_4617.accumulated.to_string()
            t_4626: 'bool15' = actual_920 == "<b>I &lt;3 <b>Ponies</b>!</b><img alt='I &lt;3 &lt;b&gt;Ponies&lt;/b&gt;!' src='ponies'>"
            def fn_4613() -> 'str13':
                return str_cat_5804("expected stringExpr(`-work/src//html/`.html, true, \"<b>\", \\interpolate, love, \"</b><img alt='\", \\interpolate, love, \"' src='ponies'>\").toString() == (", "<b>I &lt;3 <b>Ponies</b>!</b><img alt='I &lt;3 &lt;b&gt;Ponies&lt;/b&gt;!' src='ponies'>", ') not (', actual_920, ')')
            test_36.assert_(t_4626, fn_4613)
        finally:
            test_36.soft_fail_to_hard()
class TestCase55(TestCase25):
    def test___loopingInsideAnHtmlExpression__923(self) -> None:
        'looping inside an HTML expression'
        test_37: Test = Test()
        try:
            items_492: 'Sequence14[str13]' = ('One', '<Two>', 'Three')
            accumulator_38: 'SafeHtmlBuilder' = SafeHtmlBuilder()
            accumulator_38.append_safe('<ul>\n')
            def fn_4602(item_495: 'str13') -> 'None':
                accumulator_38.append_safe('  <li>')
                accumulator_38.append_string(item_495)
                accumulator_38.append_safe('</li>\n')
            list_for_each_5815(items_492, fn_4602)
            accumulator_38.append_safe('</ul>')
            got_493: 'SafeHtml' = accumulator_38.accumulated
            actual_924: 'str13' = got_493.text
            t_4611: 'bool15' = actual_924 == '<ul>\n  <li>One</li>\n  <li>&lt;Two&gt;</li>\n  <li>Three</li>\n</ul>'
            def fn_4601() -> 'str13':
                return str_cat_5804('expected got.text == (', '<ul>\n  <li>One</li>\n  <li>&lt;Two&gt;</li>\n  <li>Three</li>\n</ul>', ') not (', actual_924, ')')
            test_37.assert_(t_4611, fn_4601)
        finally:
            test_37.soft_fail_to_hard()
class TestCase56(TestCase25):
    def test___doubleQuotesInAttributeValueWithInsertedQuotes__935(self) -> None:
        'double quotes in attribute value with inserted quotes'
        test_52: Test = Test()
        try:
            t_4589: 'SafeHtmlBuilder' = SafeHtmlBuilder()
            t_4589.append_safe('<div id=a"b>')
            actual_936: 'str13' = t_4589.accumulated.text
            t_4594: 'bool15' = actual_936 == '<div id="a&#34;b">'
            def fn_4588() -> 'str13':
                return str_cat_5804('expected stringExpr(`-work/src//html/`.html, true, "<div id=a\\"b>").text == (', '<div id="a&#34;b">', ') not (', actual_936, ')')
            test_52.assert_(t_4594, fn_4588)
        finally:
            test_52.soft_fail_to_hard()
