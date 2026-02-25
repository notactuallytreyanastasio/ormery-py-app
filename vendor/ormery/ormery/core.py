from temper_core import LoggingConsole as LoggingConsole30, str_cat as str_cat10
from typing import Any as Any18, TypeVar as TypeVar19, Generic as Generic31, MutableSequence as MutableSequence12, Sequence as Sequence14, Union as Union32
from builtins import str as str13, RuntimeError as RuntimeError22, int as int17, bool as bool15, list as list5, tuple as tuple4, len as len1
from abc import ABCMeta as ABCMeta21
tuple_5778 = tuple4
list_5779 = list5
str_cat_5781 = str_cat10
len_5784 = len1
LoggingConsole30(__name__)
PART_2 = TypeVar19('PART_2', bound = Any18)
class Collector(Generic31[PART_2]):
    parts_builder_85: 'MutableSequence12[(Collected[PART_2])]'
    __slots__ = ('parts_builder_85',)
    def append_safe(this_3, fixed_87: 'str13') -> 'None':
        t_519: 'CollectedFixed[PART_2]' = CollectedFixed(fixed_87)
        this_3.parts_builder_85.append(t_519)
    def append(this_4, part_90: 'PART_2') -> 'None':
        t_517: 'CollectedPart[PART_2]' = CollectedPart(part_90)
        this_4.parts_builder_85.append(t_517)
    @property
    def parts(this_5) -> 'Sequence14[(Collected[PART_2])]':
        return tuple_5778(this_5.parts_builder_85)
    def __init__(this_39) -> None:
        t_515: 'MutableSequence12[(Collected[PART_2])]' = list_5779()
        this_39.parts_builder_85 = t_515
PART_6 = TypeVar19('PART_6', bound = Any18, covariant = True)
class Collected(Generic31[PART_6], metaclass = ABCMeta21):
    pass
PART_7 = TypeVar19('PART_7', bound = Any18)
class CollectedFixed(Collected['PART_7']):
    safe_text_95: 'str13'
    __slots__ = ('safe_text_95',)
    def __init__(this_44, safe_text_97: 'str13') -> None:
        this_44.safe_text_95 = safe_text_97
    @property
    def safe_text(this_209) -> 'str13':
        return this_209.safe_text_95
PART_8 = TypeVar19('PART_8', bound = Any18)
class CollectedPart(Collected['PART_8']):
    part_98: 'PART_8'
    __slots__ = ('part_98',)
    def __init__(this_46, part_100: 'PART_8') -> None:
        this_46.part_98 = part_100
    @property
    def part(this_212) -> 'PART_8':
        return this_212.part_98
class Context(metaclass = ABCMeta21):
    "Context encapsulates a state in a streaming parser.  It's used both to\nparse the fixed part of the content, and to pick escapers to preserve\nthe meaning of subsequent fixed parts."
    def to_string(this_9) -> 'str13':
        raise RuntimeError22()
CONTEXT_10 = TypeVar19('CONTEXT_10', bound = Context)
class AutoescState(Generic31[CONTEXT_10]):
    context_103: 'CONTEXT_10'
    subsidiary_104: 'Union32[Subsidiary, None]'
    __slots__ = ('context_103', 'subsidiary_104')
    def __init__(this_49, context_106: 'CONTEXT_10', subsidiary_107: 'Union32[Subsidiary, None]') -> None:
        this_49.context_103 = context_106
        this_49.subsidiary_104 = subsidiary_107
    @property
    def context(this_221) -> 'CONTEXT_10':
        return this_221.context_103
    @property
    def subsidiary(this_224) -> 'Union32[Subsidiary, None]':
        return this_224.subsidiary_104
CONTEXT_11 = TypeVar19('CONTEXT_11', bound = Context)
class AfterPropagate(Generic31[CONTEXT_11]):
    'AfterPropagate bundles up information about propagating context across a fixed part,\nand context transitions needed to move into a state where an interpolation is valid.'
    adjusted_string_108: 'str13'
    consumed_109: 'int17'
    state_after_110: 'AutoescState[CONTEXT_11]'
    __slots__ = ('adjusted_string_108', 'consumed_109', 'state_after_110')
    def push(this_12, delegate_112: 'Delegate', codec_113: 'Codec') -> 'AfterPropagate[CONTEXT_11]':
        "push specifies a delegate for a nested language.\nThe *Codec* is used to decode content before feeding it to the delegate, and to\nreencode the delegate's adjusted output.\n\nthis__12: AfterPropagate<CONTEXT__11>\n\ndelegate__112: Delegate\n\ncodec__113: Codec\n"
        return AfterPropagate(this_12.adjusted_string_108, this_12.consumed_109, AutoescState(this_12.state_after_110.context, Subsidiary(delegate_112, codec_113)))
    def pop(this_13) -> 'AfterPropagate[CONTEXT_11]':
        'pop undoes a push by removing a previously pushed delegate when a\nnested language region ends.\n\nthis__13: AfterPropagate<CONTEXT__11>\n'
        return AfterPropagate(this_13.adjusted_string_108, this_13.consumed_109, AutoescState(this_13.state_after_110.context, None))
    def feed(this_14, prepare_for_interp_118: 'bool15') -> 'AfterPropagate[CONTEXT_11]':
        'feed gives a nested language delegate the adjustedString, so that it\ncan reconsider it in the context of the nested language.  This may\ninvolve applying a codec to decode the content before the nested\nlanguage delegate handles it, and then re-encoding if there are any\nadjustements made by the delegate.\n\nthis__14: AfterPropagate<CONTEXT__11>\n\nprepareForInterp__118: Boolean\n'
        return_57: 'AfterPropagate[CONTEXT_11]'
        subsidiary_120: 'Union32[Subsidiary, None]' = this_14.state_after_110.subsidiary
        if not subsidiary_120 is None:
            subsidiary_237: 'Subsidiary' = subsidiary_120
            adjusted_from_delegate_121: 'str13' = feed_subsidiary_83(subsidiary_237, this_14.adjusted_string_108, prepare_for_interp_118)
            return_57 = AfterPropagate(adjusted_from_delegate_121, this_14.consumed_109, this_14.state_after_110)
        else:
            return_57 = this_14
        return return_57
    def __init__(this_52, adjusted_string_123: 'str13', consumed_124: 'int17', state_after_125: 'AutoescState[CONTEXT_11]') -> None:
        this_52.adjusted_string_108 = adjusted_string_123
        this_52.consumed_109 = consumed_124
        this_52.state_after_110 = state_after_125
    @property
    def adjusted_string(this_227) -> 'str13':
        return this_227.adjusted_string_108
    @property
    def consumed(this_230) -> 'int17':
        return this_230.consumed_109
    @property
    def state_after(this_233) -> 'AutoescState[CONTEXT_11]':
        return this_233.state_after_110
CONTEXT_15 = TypeVar19('CONTEXT_15', bound = Context, covariant = True)
class ContextPropagator(Generic31[CONTEXT_15], metaclass = ABCMeta21):
    'ContextPropagator knows how to consumes a chunk of context from a literalPart and transition\nto the Context after it.'
    def after(this_16, before_127: 'AutoescState[CONTEXT_15]', literal_part_128: 'Union32[str13, None]') -> 'AfterPropagate[CONTEXT_15]':
        "after computes the context after processing the literalPart and any\nadjustments made to the literal part.\n\nIf literalPart is null, then we're doing a context transition to get\ninto a state where we're ready to interpolate an untrusted value.\n\nthis__16: ContextPropagator<CONTEXT__15>\n\nbefore__127: AutoescState<CONTEXT__15>\n\nliteralPart__128: String | Null\n"
        raise RuntimeError22()
class Delegate(metaclass = ABCMeta21):
    'Delegate can represent an automaton for a nested language that can propagates its own state over\nstrings that relate to chunks of content from the outer language.  The content can be\ndecoded via a *Codec*.'
    def process(this_17, fixed_131: 'Union32[str13, None]') -> 'str13':
        raise RuntimeError22()
CONTEXT_18 = TypeVar19('CONTEXT_18', bound = Context, covariant = True)
class ContextDelegate(Generic31[CONTEXT_18], Delegate, metaclass = ABCMeta21):
    'ContextDelegate makes clear that a delegate uses the Context and AutoescState mechanism for parsing.'
    def process(this_22, known_141: 'Union32[str13, None]') -> 'str13':
        after_143: 'AfterPropagate[CONTEXT_18]' = propagate_over(this_22._get_context_propagator(), this_22._get_state(), known_141)
        t_479: 'AutoescState[CONTEXT_18]' = after_143.state_after
        this_22._set_state(t_479)
        return after_143.adjusted_string
class Escaper(metaclass = ABCMeta21):
    pass
CONTEXT_24 = TypeVar19('CONTEXT_24', bound = Context, covariant = True)
ESC_25 = TypeVar19('ESC_25', bound = Escaper, covariant = True)
class EscaperPicker(Generic31[CONTEXT_24, ESC_25], metaclass = ABCMeta21):
    'EscaperPicker returns the escaper that needs to be applied to untrusted parts to render them\nsafe in context.'
    def escaper_for(this_26, before_153: 'AutoescState[CONTEXT_24]') -> 'ESC_25':
        raise RuntimeError22()
CONTEXT_27 = TypeVar19('CONTEXT_27', bound = Context, covariant = True)
ESC_28 = TypeVar19('ESC_28', bound = Escaper, covariant = True)
class ContextualAutoescapingAccumulator(Generic31[CONTEXT_27, ESC_28], metaclass = ABCMeta21):
    def prepare_for_append(this_33) -> 'ESC_28':
        after_166: 'AfterPropagate[CONTEXT_27]' = propagate_over(this_33.context_propagator, this_33._get_state(), None)
        t_467: 'AutoescState[CONTEXT_27]' = after_166.state_after
        this_33._set_state(t_467)
        adjusted_167: 'str13' = after_166.adjusted_string
        if not (not adjusted_167):
            this_33.collect_fixed(adjusted_167)
        return this_33.escaper_picker.escaper_for(this_33._get_state())
    def append_safe(this_34, known_169: 'str13') -> 'None':
        after_171: 'AfterPropagate[CONTEXT_27]' = propagate_over(this_34.context_propagator, this_34._get_state(), known_169)
        t_458: 'AutoescState[CONTEXT_27]' = after_171.state_after
        this_34._set_state(t_458)
        adjusted_172: 'str13' = after_171.adjusted_string
        if not (not adjusted_172):
            this_34.collect_fixed(adjusted_172)
    def collect_fixed(this_35, fixed_fragment_174: 'str13') -> 'None':
        'Appends the fixed, trusted fragment to the collector.\n\nthis__35: ContextualAutoescapingAccumulator<CONTEXT__27, ESC__28>\n\nfixedFragment__174: String\n'
        raise RuntimeError22()
class Codec(metaclass = ABCMeta21):
    def encode(this_36, s_184: 'str13') -> 'str13':
        raise RuntimeError22()
    def decode(this_37, s_187: 'str13') -> 'str13':
        raise RuntimeError22()
class Subsidiary:
    delegate_189: 'Delegate'
    codec_190: 'Codec'
    __slots__ = ('delegate_189', 'codec_190')
    def __init__(this_81, delegate_192: 'Delegate', codec_193: 'Codec') -> None:
        this_81.delegate_189 = delegate_192
        this_81.codec_190 = codec_193
    @property
    def delegate(this_215) -> 'Delegate':
        return this_215.delegate_189
    @property
    def codec(this_218) -> 'Codec':
        return this_218.codec_190
def feed_subsidiary_83(subsidiary_176: 'Subsidiary', adjusted_str_177: 'str13', prepare_for_interp_178: 'bool15') -> 'str13':
    t_513: 'str13'
    str_180: 'str13' = adjusted_str_177
    delegate_181: 'Delegate' = subsidiary_176.delegate
    codec_182: 'Codec' = subsidiary_176.codec
    t_511: 'str13' = codec_182.decode(str_180)
    str_180 = t_511
    t_512: 'str13' = delegate_181.process(str_180)
    str_180 = t_512
    if prepare_for_interp_178:
        t_513 = delegate_181.process(None)
        str_180 = str_cat_5781(str_180, t_513)
    t_514: 'str13' = codec_182.encode(str_180)
    str_180 = t_514
    return str_180
CONTEXT_23 = TypeVar19('CONTEXT_23', bound = Context)
def propagate_over(context_propagator_144: 'ContextPropagator[CONTEXT_23]', before_145: 'AutoescState[CONTEXT_23]', known_146: 'Union32[str13, None]') -> 'AfterPropagate[CONTEXT_23]':
    'propagateOver is used by both the accumulators and context delegates to propagate context over\na known safe chunk.  Propagation is usual defined in terms of transition tables, and each\ntransition consumes some prefix of the remaining content, so this does enough transitions to\nprocess the entire chunk.\n\ncontextPropagator__144: ContextPropagator<CONTEXT__23>\n\nbefore__145: AutoescState<CONTEXT__23>\n\nknown__146: String | Null\n'
    return_66: 'AfterPropagate[CONTEXT_23]'
    t_488: 'AutoescState[CONTEXT_23]'
    t_489: 'int17'
    t_490: 'int17'
    t_491: 'str13'
    t_492: 'str13'
    t_493: 'int17'
    if known_146 is None:
        return_66 = context_propagator_144.after(before_145, None)
    else:
        known_238: 'str13' = known_146
        state_148: 'AutoescState[CONTEXT_23]' = before_145
        remainder_149: 'str13' = known_238
        adjusted_150: 'list5[str13]' = ['']
        while True:
            if not (not (not remainder_149)):
                break
            after_151: 'AfterPropagate[CONTEXT_23]' = context_propagator_144.after(state_148, remainder_149)
            adjusted_150.append(after_151.adjusted_string)
            t_488 = after_151.state_after
            state_148 = t_488
            t_489 = after_151.consumed
            t_490 = len_5784(remainder_149)
            t_491 = remainder_149[t_489 : t_490]
            remainder_149 = t_491
        t_492 = ''.join(adjusted_150)
        t_493 = len_5784(known_238)
        return_66 = AfterPropagate(t_492, t_493, state_148)
    return return_66
